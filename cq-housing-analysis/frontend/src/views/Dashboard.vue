<template>
  <div>
    <el-row :gutter="16">
      <el-col :span="6" v-for="item in cards" :key="item.label">
        <el-card>
          <div class="metric">{{ item.value }}</div>
          <div class="label">{{ item.label }}</div>
        </el-card>
      </el-col>
    </el-row>

    <el-card style="margin-top: 16px">
      <template #header>区县均价排行</template>
      <div ref="rankRef" style="height: 360px"></div>
    </el-card>
  </div>
</template>

<script setup>
import { onMounted, reactive, ref } from 'vue'
import * as echarts from 'echarts'
import { getSummary, getDistrictRank } from '@/api'

const cards = reactive([
  { label: '总房源数', value: '-' },
  { label: '覆盖区县', value: '-' },
  { label: '平均单价', value: '-' },
  { label: '平均总价', value: '-' },
])

const rankRef = ref(null)

onMounted(async () => {
  const summary = await getSummary()
  cards[0].value = summary.total_houses ?? 0
  cards[1].value = summary.total_districts ?? 0
  cards[2].value = summary.avg_unit_price ?? 0
  cards[3].value = summary.avg_total_price ?? 0

  const ranking = await getDistrictRank()
  const chart = echarts.init(rankRef.value)
  chart.setOption({
    tooltip: { trigger: 'axis' },
    xAxis: { type: 'category', data: ranking.map((r) => r.district), axisLabel: { rotate: 35 } },
    yAxis: { type: 'value' },
    series: [{ type: 'bar', data: ranking.map((r) => r.avg_price) }],
  })
})
</script>

<style scoped>
.metric {
  font-size: 24px;
  font-weight: 700;
}
.label {
  color: #6b7280;
  margin-top: 6px;
}
</style>
