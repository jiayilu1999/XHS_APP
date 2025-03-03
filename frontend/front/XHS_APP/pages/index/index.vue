<template>
	<view class="container">
		<!-- 顶部用户信息 -->
		<view class="user-info" @tap="handleUserClick">
			<image class="avatar" :src="userInfo.avatar || '/static/default-avatar.png'" mode="aspectFill"></image>
			<text class="nickname">{{ userInfo.nickname || '点击登录' }}</text>
		</view>
		
		<!-- 顶部导航栏 -->
		<view class="nav-header" :style="{ paddingTop: statusBarHeight + 'px' }">
			<text class="nav-title">小红书文案生成器</text>
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
						@tap="handleFeature(item)"
					>
						<image class="grid-item-icon" :src="item.icon" :alt="item.name" />
						<view class="grid-item-title">{{ item.name }}</view>
						<view class="grid-item-desc">{{ item.desc }}</view>
					</view>
				</view>
			</view>
		</view>

		<!-- 底部导航栏 -->
		<view class="tab-bar">
			<view class="tab-item active" @tap="switchTab('index')">
				<text class="tab-icon">首页</text>
			</view>
			<view class="tab-item" @tap="switchTab('mine')">
				<text class="tab-icon">我的</text>
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
						icon: '/static/icons/rewrite.png',
						name: '改写助手',
						desc: '智能排版，由AI改写',
						type: 'rewrite'
					},
					{
						icon: '/static/icons/title.png',
						name: '爆款标题',
						desc: '新手自媒体必备神器',
						type: 'title'
					},
					{
						icon: '/static/icons/translate.png',
						name: '翻译助手',
						desc: 'AI翻译成多种语言',
						type: 'translate'
					},
					{
						icon: '/static/icons/note.png',
						name: '识图写笔记',
						desc: 'AI识别图片内容，生成笔记',
						type: 'note'
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
			// 处理功能卡片点击
			handleFeature(item) {
				console.log('尝试跳转到:', `/pages/feature/feature?type=${item.type}`);
				uni.navigateTo({
					url: `/pages/feature/feature?type=${item.type}`,
					success: () => {
						console.log('跳转成功');
					},
					fail: (err) => {
						console.error('导航失败：', err);
						// 添加更详细的错误提示
						uni.showToast({
							title: `跳转失败: ${err.errMsg}`,
							icon: 'none',
							duration: 2000
						});
					}
				});
			},
			// 处理底部标签页切换
			switchTab(page) {
				const url = page === 'index' ? '/pages/index/index' : '/pages/mine/mine';
				console.log('尝试切换到:', url);
				uni.switchTab({
					url,
					success: () => {
						console.log('切换成功');
					},
					fail: (err) => {
						console.error('切换标签页失败：', err);
						// 添加更详细的错误提示
						uni.showToast({
							title: `切换失败: ${err.errMsg}`,
							icon: 'none',
							duration: 2000
						});
					}
				});
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
