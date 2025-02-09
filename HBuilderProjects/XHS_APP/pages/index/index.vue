<template>
	<view class="container">
		<!-- 顶部导航栏 -->
		<view class="nav-header" :style="{ paddingTop: statusBarHeight + 'px' }">
			<text class="nav-title">红薯通AI</text>
			<view class="nav-right">
				<text class="settings-icon">⚙️</text>
			</view>
		</view>
		
		<!-- 主要内容区域 -->
		<view class="main-content" :style="{ paddingTop: (statusBarHeight + 44) + 'px' }">
			<!-- Banner -->
			<view class="banner">
				<image src="/static/banner.png" mode="aspectFill" />
			</view>
			
			<!-- 功能卡片网格 -->
			<view class="content">
				<view class="grid-container">
					<view 
						class="grid-item" 
						v-for="(item, index) in features" 
						:key="index"
						@tap="navigateToFeature(item)"
					>
						<image class="grid-item-icon" :src="item.icon" mode="aspectFit" />
						<text class="grid-item-title">{{ item.title }}</text>
						<text class="grid-item-desc">{{ item.desc }}</text>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				statusBarHeight: 20,
				features: [
					{
						icon: '/static/icons/edit.png',
						title: '改写助手',
						desc: '智能排版，由AI改写',
						path: '/pages/feature/feature'
					},
					{
						icon: '/static/icons/translate.png',
						title: '翻译助手',
						desc: '多语言翻译，由AI完成',
						path: '/pages/feature/feature'
					},
					{
						icon: '/static/icons/summarize.png',
						title: '摘要助手',
						desc: '智能摘要，由AI生成',
						path: '/pages/feature/feature'
					},
					{
						icon: '/static/icons/grammar.png',
						title: '语法助手',
						desc: '语法检查，由AI完成',
						path: '/pages/feature/feature'
					}
				]
			}
		},
		onLoad() {
			// 获取状态栏高度
			const systemInfo = uni.getSystemInfoSync()
			this.statusBarHeight = systemInfo.statusBarHeight
		},
		methods: {
			navigateToFeature(item) {
				uni.navigateTo({
					url: item.path + '?title=' + item.title + '&type=' + item.title,
					fail: (err) => {
						console.error('导航失败:', err)
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
		background-color: #f5f5f5;
	}

	.nav-header {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		height: 44px;
		background: #fff;
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 0 30rpx;
		z-index: 100;
		
		.nav-title {
			font-size: 36rpx;
			font-weight: bold;
			color: #333;
		}
		
		.settings-icon {
			font-size: 40rpx;
		}
	}

	.main-content {
		padding: 30rpx;
	}

	.banner {
		width: 100%;
		height: 300rpx;
		border-radius: 24rpx;
		overflow: hidden;
		margin-bottom: 30rpx;
		
		image {
			width: 100%;
			height: 100%;
		}
	}

	.content {
		padding: 20rpx;
	}

	.grid-container {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 24rpx;
		padding: 10rpx;
	}

	.grid-item {
		background: #fff;
		border-radius: 20rpx;
		padding: 24rpx 20rpx;
		display: flex;
		flex-direction: column;
		align-items: center;
		text-align: center;
		box-shadow: 0 2rpx 12rpx rgba(0, 0, 0, 0.03);
		transition: all 0.3s ease;
		aspect-ratio: 1;
		width: 100%;
		box-sizing: border-box;
		
		&:active {
			transform: scale(0.98);
			opacity: 0.9;
		}
	}

	.grid-item-icon {
		width: 64rpx;
		height: 64rpx;
		margin-bottom: 16rpx;
		flex-shrink: 0;
	}

	.grid-item-title {
		font-size: 28rpx;
		font-weight: 600;
		color: #333;
		margin-bottom: 8rpx;
		flex-shrink: 0;
	}

	.grid-item-desc {
		font-size: 22rpx;
		color: #999;
		line-height: 1.4;
		display: -webkit-box;
		-webkit-box-orient: vertical;
		-webkit-line-clamp: 2;
		overflow: hidden;
		flex: 1;
		width: 100%;
	}
</style>
