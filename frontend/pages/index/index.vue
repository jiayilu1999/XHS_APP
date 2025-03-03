<template>
  <!-- No changes to template section -->
</template>

<script>
export default {
  methods: {
    handleFeature(item) {
      uni.navigateTo({
        url: `/feature?type=${item.type}`,
        fail: (err) => {
          console.error('导航失败：', err)
          uni.showToast({
            title: '页面跳转失败',
            icon: 'none'
          })
        }
      })
    },
    switchTab(page) {
      const url = page === 'index' ? '/index' : '/mine'
      uni.switchTab({
        url,
        fail: (err) => {
          console.error('切换标签页失败：', err)
          uni.showToast({
            title: '页面切换失败',
            icon: 'none'
          })
        }
      })
    }
  }
}
</script>

<style>
  /* No changes to style section */
</style> 