<script>
export default {
  onLaunch: function() {
    console.log('App Launch')
  },
  onShow: function() {
    console.log('App Show')
  },
  onHide: function() {
    console.log('App Hide')
  }
}
</script>

<style>
/* 全局样式 */
page {
  background-color: #f5f5f5;
  font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica,
    Segoe UI, Arial, Roboto, 'PingFang SC', 'miui', 'Hiragino Sans GB', 'Microsoft Yahei',
    sans-serif;
}

/* 去除按钮默认边框 */
button::after {
  border: none;
}

/* 统一图标大小 */
.tab-icon {
  width: 48rpx;
  height: 48rpx;
}

/* 统一内容区域样式 */
.container {
  min-height: 100vh;
  box-sizing: border-box;
}

/* 统一列表样式 */
.list-item {
  background-color: #ffffff;
  padding: 20rpx 30rpx;
  margin-bottom: 2rpx;
}

/* 统一卡片样式 */
.card {
  background-color: #ffffff;
  border-radius: 12rpx;
  padding: 20rpx;
  margin: 20rpx;
  box-shadow: 0 2rpx 4rpx rgba(0, 0, 0, 0.1);
}
</style>
