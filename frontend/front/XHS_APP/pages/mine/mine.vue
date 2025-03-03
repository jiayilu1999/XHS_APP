<template>
  <view class="container">
    <!-- 顶部导航栏 -->
    <view class="header">
      <text class="title">我的</text>
    </view>
    
    <!-- 用户信息区域 -->
    <view class="user-info" @tap="handleLogin">
      <image class="avatar" :src="userInfo.avatar || '/static/default-avatar.png'" mode="aspectFill"></image>
      <view class="info">
        <text class="nickname">{{ userInfo.nickname || '点击登录' }}</text>
        <text class="desc" v-if="userInfo.isLogin">{{ userInfo.phone }}</text>
      </view>
    </view>
    
    <!-- 功能列表 -->
    <view class="feature-list">
      <view class="feature-item" v-for="(item, index) in features" :key="index" @tap="handleFeature(item)">
        <text class="feature-icon">{{ item.icon }}</text>
        <text class="feature-name">{{ item.name }}</text>
        <text class="arrow">></text>
      </view>
    </view>
    
    <!-- 版本信息 -->
    <view class="version-info">
      <text class="version-text">当前版本 1.0.0</text>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      userInfo: {},
      features: [
        { icon: '⭐️', name: '我的收藏', path: '/pages/collection/collection' },
        { icon: '🔔', name: '消息通知', path: '/pages/notification/notification' },
        { icon: '⚙️', name: '设置', path: '/pages/settings/settings' },
        { icon: '❓', name: '帮助与反馈', path: '/pages/help/help' }
      ]
    }
  },
  onShow() {
    this.checkLoginStatus()
  },
  methods: {
    checkLoginStatus() {
      const userInfo = uni.getStorageSync('userInfo')
      if (userInfo) {
        this.userInfo = JSON.parse(userInfo)
      }
    },
    handleLogin() {
      if (!this.userInfo.isLogin) {
        uni.navigateTo({
          url: '/pages/login/login',
          fail: (err) => {
            console.error('跳转登录页失败：', err)
            uni.showToast({
              title: '页面跳转失败',
              icon: 'none'
            })
          }
        })
      }
    },
    handleFeature(item) {
      uni.navigateTo({
        url: item.path,
        fail: (err) => {
          console.error('跳转功能页失败：', err)
          uni.showToast({
            title: '页面跳转失败',
            icon: 'none'
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
}

.header {
  padding: 20rpx 30rpx;
  background: #fff;
  
  .title {
    font-size: 36rpx;
    font-weight: bold;
    color: #333;
  }
}

.user-info {
  margin: 20rpx;
  background: #fff;
  border-radius: 16rpx;
  padding: 30rpx;
  display: flex;
  align-items: center;
  
  .avatar {
    width: 120rpx;
    height: 120rpx;
    border-radius: 60rpx;
    margin-right: 20rpx;
  }
  
  .info {
    flex: 1;
    
    .nickname {
      font-size: 32rpx;
      font-weight: bold;
      color: #333;
      margin-bottom: 10rpx;
    }
    
    .desc {
      font-size: 24rpx;
      color: #999;
    }
  }
}

.feature-list {
  margin: 20rpx;
  background: #fff;
  border-radius: 16rpx;
  
  .feature-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 30rpx;
    border-bottom: 1rpx solid #f5f5f5;
    
    &:last-child {
      border-bottom: none;
    }
    
    .feature-icon {
      font-size: 36rpx;
      margin-right: 20rpx;
    }
    
    .feature-name {
      font-size: 28rpx;
      color: #333;
    }
    
    .arrow {
      font-size: 28rpx;
      color: #999;
    }
  }
}

.version-info {
  text-align: center;
  padding: 40rpx;
  
  .version-text {
    font-size: 24rpx;
    color: #999;
  }
}
</style> 