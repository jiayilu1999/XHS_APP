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
      pageTitle: '',
      pageType: '',
      inputText: '',
      textLength: 1100,
      currentStyle: 0,
      styles: ['日常风格', '可爱风格', '商务风格', '幽默风格'],
      placeholder: '写下你想要改写的内容，AI将帮你生成更好的表达查看示例'
    }
  },
  onLoad(options) {
    this.pageTitle = options.title || '功能页面'
    this.pageType = options.type || ''
    // 根据不同类型设置不同的placeholder
    switch(this.pageType) {
      case '改写助手':
        this.placeholder = '写下你想要改写的内容，AI将帮你生成更好的表达'
        break
      case '翻译助手':
        this.placeholder = '写下你想要翻译的内容'
        break
      case '摘要助手':
        this.placeholder = '写下你想要生成摘要的内容'
        break
      case '语法助手':
        this.placeholder = '写下你想要检查语法的内容'
        break
      default:
        break
    }
  },
  methods: {
    goBack() {
      uni.navigateBack()
    },
    onLengthChange(e) {
      this.textLength = e.detail.value
    },
    selectStyle(index) {
      this.currentStyle = index
    },
    generateContent() {
      if (!this.inputText.trim()) {
        uni.showToast({
          title: '请输入内容',
          icon: 'none'
        })
        return
      }
      // TODO: 调用生成接口
      console.log('生成内容', {
        type: this.pageType,
        text: this.inputText,
        length: this.textLength,
        style: this.styles[this.currentStyle]
      })
    },
	async rewriteNote() {
		console.log("here !")
			const content = "ff"
			const style = "可爱风格"
			const maxWords = "2000"
	  	    const url = `http://localhost:8000/api1_red_note_rewrite?content=${encodeURIComponent(content)}&style=${encodeURIComponent(style)}&max_words=${maxWords}`;
	  	
	  	    try {
	  	                const response = await fetch(url, {
	  	                    method: 'POST',
	  	                    headers: {
	  	                        'Accept': 'application/json'
	  	                    },
	  	                    body: {
								"content":content,
								"style":style,
								"max_words": maxWords
							} // 空 body，按照你的接口定义
	  	                });
	  	    
	  	                if (!response.ok) {
	  	                    throw new Error(`HTTP error! Status: ${response.status}`);
	  	                }
	  	    
	  	                const result = await response.json();
	  	                console.log("API返回的结果:", result);
	  	                // 可以在这里处理 API 返回的数据，比如更新 Vue 组件的数据
	  	            } catch (error) {
	  	                console.error('调用 API 失败:', error);
	  	            }
	  	        }
	  	    }
}
</script>

<style lang="scss">
.container {
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
    
    .input-area {
      position: relative;
      margin-bottom: 30rpx;
      
      .input-text {
        width: 100%;
        height: 300rpx;
        padding: 20rpx;
        background: #fff;
        border-radius: 20rpx;
        font-size: 28rpx;
      }
      
      .word-count {
        position: absolute;
        right: 20rpx;
        bottom: 20rpx;
        font-size: 24rpx;
        color: #999;
      }
    }
    
    .advanced-options {
      margin-bottom: 30rpx;
      
      .section-title {
        font-size: 28rpx;
        font-weight: bold;
        margin-bottom: 20rpx;
      }
      
      .option-item {
        display: flex;
        align-items: center;
        margin-bottom: 20rpx;
        
        text {
          flex: 1;
          font-size: 26rpx;
          color: #666;
        }
        
        .length-slider {
          flex: 2;
        }
      }
    }
    
    .style-options {
      display: flex;
      flex-wrap: wrap;
      gap: 20rpx;
      margin-bottom: 30rpx;
      
      .style-item {
        padding: 15rpx 30rpx;
        background: #f5f5f5;
        border-radius: 30rpx;
        font-size: 26rpx;
        color: #666;
        
        &.active {
          background: #ff4444;
          color: #fff;
        }
      }
    }
    
    .generate-btn {
      width: 100%;
      height: 88rpx;
      line-height: 88rpx;
      background: #ff4444;
      color: #fff;
      border-radius: 44rpx;
      font-size: 32rpx;
      margin: 30rpx 0;
    }
  }
}
</style>