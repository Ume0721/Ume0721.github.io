<template>
  <div>
    <el-row :gutter="16">
      <el-col :span="8">
        <el-card>
          <template #header>
            预测模型
            <el-button style="float: right" type="primary" size="small" @click="runPrediction">运行</el-button>
          </template>
          <pre>{{ predictionText }}</pre>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card>
          <template #header>
            聚类分析
            <el-button style="float: right" type="primary" size="small" @click="runClustering">运行</el-button>
          </template>
          <pre>{{ clusteringText }}</pre>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card>
          <template #header>
            相关性
            <el-button style="float: right" type="primary" size="small" @click="runCorrelation">运行</el-button>
          </template>
          <pre>{{ correlationText }}</pre>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { getClustering, getCorrelation, getPrediction } from '@/api'

const predictionText = ref('尚未运行')
const clusteringText = ref('尚未运行')
const correlationText = ref('尚未运行')

async function runPrediction() {
  const res = await getPrediction()
  predictionText.value = JSON.stringify(res, null, 2)
}

async function runClustering() {
  const res = await getClustering({ n_clusters: 5 })
  clusteringText.value = JSON.stringify(res, null, 2)
}

async function runCorrelation() {
  const res = await getCorrelation()
  correlationText.value = JSON.stringify(res, null, 2)
}
</script>
