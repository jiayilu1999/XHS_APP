<template>
  <view class="container">
    <view class="login-box">
      <view class="header">
        <text class="title">登录</text>
      </view>
      
      <view class="input-group">
        <view class="input-item">
          <text class="label">手机号</text>
          <input type="number" v-model="phone" placeholder="请输入手机号" maxlength="11" />
        </view>
        <view class="input-item">
          <text class="label">验证码</text>
          <input type="number" v-model="code" placeholder="请输入验证码" maxlength="6" />
          <button class="code-btn" @tap="getCode" :disabled="counting > 0">
            {{counting > 0 ? `${counting}s` : '获取验证码'}}
          </button>
        </view>
      </view>
      
      <button class="login-btn" @tap="handleLogin">登录</button>
      
      <view class="tips">
        <text>登录即代表同意</text>
        <text class="link">《用户协议》</text>
        <text>和</text>
        <text class="link">《隐私政策》</text>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      phone: '',
      code: '',
      counting: 0
    }
  },
  methods: {
    getCode() {
      if (!/^1[3-9]\d{9}$/.test(this.phone)) {
        uni.showToast({
          title: '请输入正确的手机号',
          icon: 'none'
        })
        return
      }
      
      this.counting = 60
      const timer = setInterval(() => {
        this.counting--
        if (this.counting <= 0) {
          clearInterval(timer)
        }
      }, 1000)
      
      // TODO: 调用获取验证码接口
      uni.showToast({
        title: '验证码已发送',
        icon: 'success'
      })
    },
    
    handleLogin() {
      if (!/^1[3-9]\d{9}$/.test(this.phone)) {
        uni.showToast({
          title: '请输入正确的手机号',
          icon: 'none'
        })
        return
      }
      
      if (!/^\d{6}$/.test(this.code)) {
        uni.showToast({
          title: '请输入正确的验证码',
          icon: 'none'
        })
        return
      }
      
      // 登录成功后的处理
      const userInfo = {
        avatar: '/static/default-avatar.png',
        nickname: '用户' + this.phone.substr(-4),
        isLogin: true,
        phone: this.phone
      }
      
      // 保存用户信息
      uni.setStorageSync('userInfo', JSON.stringify(userInfo))
      
      // 返回上一页
      uni.navigateBack({
        delta: 1,
        success: () => {
          // 刷新上一页数据
          const pages = getCurrentPages()
          const prevPage = pages[pages.length - 2]
          if (prevPage && prevPage.checkLoginStatus) {
            prevPage.checkLoginStatus()
          }
        },
        fail: (err) => {
          console.error('返回失败：', err)
          // 如果返回失败，跳转到首页
          uni.switchTab({
            url: '/pages/index/index'
          })
        }
      })
    }
  }
}
</script>

<style lang="scss">
.container {
  min-height: 100vh;
  background: #f5f5f5;
  padding: 30rpx;
}

.login-box {
  background: #fff;
  border-radius: 16rpx;
  padding: 30rpx;
  
  .header {
    text-align: center;
    margin-bottom: 40rpx;
    
    .title {
      font-size: 36rpx;
      font-weight: bold;
      color: #333;
    }
  }
  
  .input-group {
    margin-bottom: 40rpx;
    
    .input-item {
      position: relative;
      margin-bottom: 30rpx;
      
      .label {
        font-size: 28rpx;
        color: #333;
        margin-bottom: 20rpx;
        display: block;
      }
      
      input {
        width: 100%;
        height: 88rpx;
        background: #f8f8f8;
        border-radius: 8rpx;
        padding: 0 30rpx;
        font-size: 28rpx;
      }
      
      .code-btn {
        position: absolute;
        right: 20rpx;
        top: 50%;
        transform: translateY(-50%);
        font-size: 24rpx;
        color: #ff2442;
        background: none;
        padding: 0;
        
        &[disabled] {
          color: #999;
        }
        
        &::after {
          display: none;
        }
      }
    }
  }
  
  .login-btn {
    width: 100%;
    height: 88rpx;
    background: #ff2442;
    color: #fff;
    font-size: 32rpx;
    border-radius: 44rpx;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 30rpx;
  }
  
  .tips {
    text-align: center;
    font-size: 24rpx;
    color: #999;
    
    .link {
      color: #ff2442;
    }
  }
}
</style> 