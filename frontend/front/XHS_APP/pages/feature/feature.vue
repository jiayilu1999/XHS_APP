<template>
  <view class="container">
    <!-- 顶部导航栏 -->
    <view class="header">
      <view class="back" @tap="goBack">
        <text class="back-icon">←</text>
      </view>
      <text class="title">{{pageTitle}}</text>
    </view>
    
    <!-- 主要内容区域 -->
    <view class="content">
      <!-- 输入区域 -->
      <textarea
        v-model="inputText"
        class="input-area"
        :placeholder="placeholder"
        :maxlength="2000"
      />
      <text class="word-count">{{inputText.length}}/2000</text>
      
      <!-- 高级选项 -->
      <view class="advanced-options">
        <text class="section-title">高级选项</text>
        <view class="option-item">
          <text>文章长度</text>
          <slider
            :value="textLength"
            :min="100"
            :max="2000"
            :step="100"
            @change="onLengthChange"
            show-value
            class="length-slider"
          />
        </view>
      </view>
      
      <!-- 风格选择 -->
      <view class="style-options">
        <view 
          v-for="(style, index) in styles" 
          :key="index"
          class="style-item"
          :class="{ active: currentStyle === index }"
          @tap="selectStyle(index)"
        >
          {{ style }}
        </view>
      </view>
      
      <!-- 生成按钮 -->
      <button class="generate-btn" @tap="rewriteNote">开始生成</button>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      type: '',
      inputText: '',
      imagePath: '',
      pageTitle: '',
      pageType: '',
      textLength: 1100,
      currentStyle: 0,
      styles: ['日常风格', '可爱风格', '商务风格', '幽默风格'],
      placeholder: '写下你想要改写的内容，AI将帮你生成更好的表达查看示例'
    }
  },
  onLoad(options) {
    // 获取路由参数
    this.type = options.type
    // 设置页面标题
    const titles = {
      rewrite: '改写助手',
      title: '爆款标题',
      translate: '翻译助手',
      note: '识图写笔记'
    }
    uni.setNavigationBarTitle({
      title: titles[this.type] || '功能'
    })
  },
  methods: {
    // 返回首页
    goBack() {
      uni.navigateBack({
        delta: 1,
        fail: (err) => {
          console.error('返回失败：', err)
          uni.switchTab({
            url: '/pages/index/index'
          })
        }
      })
    },
    handleSubmit() {
      // 根据不同类型处理提交
      switch(this.type) {
        case 'rewrite':
          if (!this.inputText.trim()) {
            uni.showToast({
              title: '请输入需要改写的内容',
              icon: 'none'
            })
            return
          }
          break
        case 'title':
          if (!this.inputText.trim()) {
            uni.showToast({
              title: '请输入文章内容',
              icon: 'none'
            })
            return
          }
          break
        case 'translate':
          if (!this.inputText.trim()) {
            uni.showToast({
              title: '请输入需要翻译的内容',
              icon: 'none'
            })
            return
          }
          break
        case 'note':
          if (!this.imagePath) {
            uni.showToast({
              title: '请先上传图片',
              icon: 'none'
            })
            return
          }
          break
      }
      
      // TODO: 调用对应的API处理
      uni.showLoading({
        title: '处理中...'
      })
      
      setTimeout(() => {
        uni.hideLoading()
        uni.showToast({
          title: '功能开发中',
          icon: 'none'
        })
      }, 1500)
    },
    handleLanguageChange(e) {
      this.selectedLanguageIndex = e.detail.value
    },
    chooseImage() {
      uni.chooseImage({
        count: 1,
        success: (res) => {
          this.imagePath = res.tempFilePaths[0]
        }
      })
    }
  }
}
</script>

<style lang="scss">
.container {
  padding: 20rpx;
  
  .feature-content {
    background: #fff;
    border-radius: 12rpx;
    padding: 20rpx;
    
    .feature-section {
      .input-area {
        margin-bottom: 20rpx;
        
        .input-text {
          width: 100%;
          height: 300rpx;
          background: #f5f5f5;
          border-radius: 8rpx;
          padding: 20rpx;
          box-sizing: border-box;
        }
      }
      
      .language-select {
        margin-bottom: 20rpx;
        
        .picker {
          padding: 20rpx;
          background: #f5f5f5;
          border-radius: 8rpx;
        }
      }
      
      .upload-area {
        width: 100%;
        height: 400rpx;
        background: #f5f5f5;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 20rpx;
        border-radius: 8rpx;
        
        .upload-tip {
          color: #999;
          font-size: 28rpx;
        }
        
        .preview-image {
          width: 100%;
          height: 100%;
          border-radius: 8rpx;
        }
      }
      
      .submit-btn {
        width: 100%;
        height: 88rpx;
        background: #ff2442;
        color: #fff;
        border-radius: 44rpx;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 32rpx;
        margin-top: 40rpx;
      }
    }
  }
}
</style>