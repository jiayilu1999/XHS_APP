<template>
  <view class="history-container">
    <view class="header">
      <view class="back" @tap="goBack">
        <text class="iconfont icon-back">←</text>
      </view>
      <text class="title">历史记录</text>
    </view>
    
    <view class="content">
      <view class="history-list">
        <view class="history-item" v-for="(item, index) in historyList" :key="index">
          <view class="item-header">
            <text class="item-type">{{item.type}}</text>
            <text class="item-time">{{item.time}}</text>
          </view>
          <view class="item-content">{{item.content}}</view>
          <view class="item-actions">
            <button class="action-btn copy" @tap="copyContent(item.content)">复制</button>
            <button class="action-btn delete" @tap="deleteItem(index)">删除</button>
          </view>
        </view>
      </view>
      
      <view class="empty-state" v-if="!historyList.length">
        <text class="empty-text">暂无历史记录</text>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      historyList: []
    }
  },
  onLoad() {
    this.historyList = this.$store.state.generationHistory
  },
  methods: {
    goBack() {
      uni.navigateBack()
    },
    copyContent(content) {
      uni.setClipboardData({
        data: content,
        success: () => {
          uni.showToast({
            title: '已复制到剪贴板',
            icon: 'success'
          })
        }
      })
    },
    deleteItem(index) {
      this.$store.commit('DELETE_HISTORY_ITEM', index)
      this.historyList = this.$store.state.generationHistory
    }
  }
}
</script>

<style lang="scss">
.history-container {
  .header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 88rpx;
    background: #fff;
    display: flex;
    align-items: center;
    padding: 0 30rpx;
    border-bottom: 1rpx solid #eee;
    z-index: 100;
    
    .back {
      padding: 20rpx;
      margin-left: -20rpx;
    }
    
    .title {
      flex: 1;
      text-align: center;
      font-size: 32rpx;
      font-weight: bold;
    }
  }
  
  .content {
    margin-top: 88rpx;
    padding: 30rpx;
    
    .history-list {
      .history-item {
        background: #fff;
        border-radius: 20rpx;
        padding: 30rpx;
        margin-bottom: 30rpx;
        
        .item-header {
          display: flex;
          justify-content: space-between;
          margin-bottom: 20rpx;
          
          .item-type {
            font-size: 28rpx;
            font-weight: bold;
            color: #333;
          }
          
          .item-time {
            font-size: 24rpx;
            color: #999;
          }
        }
        
        .item-content {
          font-size: 28rpx;
          line-height: 1.6;
          color: #666;
          margin-bottom: 20rpx;
        }
        
        .item-actions {
          display: flex;
          gap: 20rpx;
          
          .action-btn {
            flex: 1;
            height: 70rpx;
            line-height: 70rpx;
            border-radius: 35rpx;
            font-size: 26rpx;
            
            &.copy {
              background: #f5f5f5;
              color: #666;
            }
            
            &.delete {
              background: #ff4444;
              color: #fff;
            }
          }
        }
      }
    }
    
    .empty-state {
      text-align: center;
      padding: 100rpx 0;
      
      .empty-text {
        font-size: 28rpx;
        color: #999;
      }
    }
  }
}
</style>