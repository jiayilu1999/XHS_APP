<template>
  <view class="container">
    <!-- 顶部导航栏 -->
    <view class="header">
      <text class="title">我的</text>
    </view>
    
    <!-- 用户信息 -->
    <view class="user-info">
      <image class="avatar" src="/static/default-avatar.png" mode="aspectFill"/>
      <view class="info">
        <text class="nickname">未登录</text>
        <text class="desc">登录体验更多功能</text>
      </view>
      <button class="login-btn" @tap="login">登录</button>
    </view>
    
    <!-- 功能列表 -->
    <view class="feature-list">
      <view class="feature-item" v-for="(item, index) in features" :key="index" @tap="handleFeature(item)">
        <view class="item-left">
          <text class="item-icon">{{item.icon}}</text>
          <text class="item-name">{{item.name}}</text>
        </view>
        <text class="item-arrow">→</text>
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
      features: [
        { icon: '⭐️', name: '我的收藏', path: '/pages/collection/collection' },
        { icon: '🔔', name: '消息通知', path: '/pages/notification/notification' },
        { icon: '⚙️', name: '设置', path: '/pages/settings/settings' },
        { icon: '❓', name: '帮助与反馈', path: '/pages/help/help' }
      ]
    }
  },
  methods: {
    login() {
      uni.showToast({
        title: '登录功能开发中',
        icon: 'none'
      })
    },
    handleFeature(item) {
      uni.showToast({
        title: '功能开发中',
        icon: 'none'
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
  
  .login-btn {
    background: #ff2442;
    color: #fff;
    font-size: 28rpx;
    padding: 10rpx 30rpx;
    border-radius: 30rpx;
    margin: 0;
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
    
    .item-left {
      display: flex;
      align-items: center;
      
      .item-icon {
        font-size: 36rpx;
        margin-right: 20rpx;
      }
      
      .item-name {
        font-size: 28rpx;
        color: #333;
      }
    }
    
    .item-arrow {
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