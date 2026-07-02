<template>
  <div>
    <el-card>
      <el-form inline>
        <el-form-item label="区县">
          <el-select v-model="filters.district" clearable>
            <el-option v-for="d in districts" :key="d.district" :label="d.district" :value="d.district" />
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="fetchData">筛选</el-button>
          <el-button @click="seed">生成模拟数据</el-button>
          <el-button type="danger" plain @click="clear">清空数据</el-button>
        </el-form-item>
      </el-form>
    </el-card>

    <el-card style="margin-top: 16px">
      <el-table :data="tableData" v-loading="loading" border>
        <el-table-column prop="district" label="区县" width="100" />
        <el-table-column prop="community" label="小区" min-width="140" />
        <el-table-column prop="layout" label="户型" width="100" />
        <el-table-column prop="area" label="面积" width="100" />
        <el-table-column prop="total_price" label="总价(万)" width="120" />
        <el-table-column prop="unit_price" label="单价(元/㎡)" width="130" />
      </el-table>
    </el-card>
  </div>
</template>

<script setup>
import { onMounted, reactive, ref } from 'vue'
import { ElMessage } from 'element-plus'
import { clearData, getDistricts, getHouseList, seedMockData } from '@/api'

const loading = ref(false)
const tableData = ref([])
const districts = ref([])
const filters = reactive({ district: null })

async function fetchData() {
  loading.value = true
  try {
    const res = await getHouseList({ page: 1, page_size: 50, district: filters.district })
    tableData.value = res.data
  } finally {
    loading.value = false
  }
}

async function seed() {
  await seedMockData(10000)
  ElMessage.success('已生成 10000 条模拟数据')
  await refresh()
}

async function clear() {
  await clearData()
  ElMessage.success('数据已清空')
  await refresh()
}

async function refresh() {
  districts.value = await getDistricts()
  await fetchData()
}

onMounted(refresh)
</script>
