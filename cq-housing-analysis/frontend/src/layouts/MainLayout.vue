<template>
  <el-container class="layout">
    <el-aside width="220px" class="aside">
      <div class="brand">CQ 房价分析</div>
      <el-menu :default-active="$route.path" router>
        <el-menu-item index="/">数据概览</el-menu-item>
        <el-menu-item index="/explorer">数据浏览</el-menu-item>
        <el-menu-item index="/analysis">智能分析</el-menu-item>
      </el-menu>
    </el-aside>
    <el-container>
      <el-header class="header">重庆市二手房价格分析系统</el-header>
      <el-main class="main">
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<style scoped>
.layout {
  min-height: 100vh;
}
.aside {
  border-right: 1px solid #e5e7eb;
  background: #fafafa;
}
.brand {
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
}
.header {
  background: #fff;
  border-bottom: 1px solid #e5e7eb;
  display: flex;
  align-items: center;
  font-weight: 600;
}
.main {
  background: #f5f7fa;
}
</style>
