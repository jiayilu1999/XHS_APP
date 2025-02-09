<template>
  <view class="container">
    <view class="header">
      <text class="title">素材库</text>
    </view>
    
    <view class="content">
      <!-- 这里添加素材库的内容 -->
      <text>素材库内容</text>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      
    }
  },
  methods: {
    
  }
}
</script>

<style lang="scss">
.container {
  min-height: 100vh;
  background-color: #f5f5f5;
}

.header {
  padding: 20rpx 30rpx;
  background-color: #fff;
  
  .title {
    font-size: 36rpx;
    font-weight: bold;
    color: #333;
  }
}

.content {
  padding: 30rpx;
}
</style> 