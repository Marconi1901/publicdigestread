<template>
  <div class="app">
    <h1>书摘集锦 感悟人生</h1>
    <div class="quotes-container">
      <QuoteCard v-for="quote in quotes" :key="quote.id" :quote="quote" />
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import QuoteCard from './components/QuoteCard.vue'

export default {
  name: 'App',
  components: {
    QuoteCard
  },
  setup() {
    const quotes = ref([])

    const fetchQuotes = async () => {
      try {
        const response = await axios.get('/api/quotes/random/4')
        quotes.value = response.data // 更新响应式变量
      } catch (error) {
        console.error('请求失败:', error)
        quotes.value = [
          { id: 1, content: "生命中最美好的事物总是在你意想不到的时候出现。", bookname: "百年孤独", author: "加西亚·马尔克斯" },
          { id: 2, content: "弱小和无知不是生存的障碍，傲慢才是。", bookname: "三体", author: "刘慈欣" },
          { id: 3, content: "人是为活着本身而活着，而不是为了活着之外的任何事物所活着。", bookname: "活着", author: "余华" },
          { id: 4, content: "生活就是这样，在绝望中孕育希望，在希望中走向绝望。", bookname: "平凡的世界", author: "路遥" }
        ]
      }
    }

    onMounted(() => {
      fetchQuotes()
    })

    return {
      quotes
    }
  }
}
</script>

<style>
.app {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.quotes-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}
</style>