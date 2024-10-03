<template>
    <div class="quote-card" :style="{ backgroundColor: cardColor }">
      <p class="quote-text">"{{ quote.content }}"</p>
      <p class="quote-book">—— 《{{ quote.bookname }}》</p>
      <p class="quote-author">{{ quote.author }}</p>
    </div>
  </template>
  
  <script>
  import { computed } from 'vue'
  
  export default {
    name: 'QuoteCard',
    props: {
      quote: {
        type: Object,
        required: true
      }
    },
    setup() {
      const colors = [
        '#FFB3BA', '#BAFFC9', '#BAE1FF', '#FFFFBA', 
        '#FFDFBA', '#E0BBE4', '#957DAD', '#D291BC',
        '#B5EAD7', '#C7CEEA', '#FFDAC1', '#FF9AA2',
        '#F1CBFF', '#CFBAF0', '#A3C4F3', '#90DBF4',
        '#8EECF5', '#98F5E1', '#B9FBC0', '#F1C0E8',
        '#CFDFDA', '#F6EAC2', '#FFB7C5', '#ADCBE3',
        '#FF5733', '#33FF57', '#3357FF', '#F1C40F',
        '#9B59B6', '#1ABC9C', '#E74C3C', '#2ECC71', 
        '#3498DB', '#E67E22'
      ]
  
      const cardColor = computed(() => {
        return colors[Math.floor(Math.random() * colors.length)]
      })
  
      return {
        cardColor
      }
    }
  }
  </script>
  
  <style scoped>
  .quote-card {
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
  }
  
  .quote-card:hover {
    transform: translateY(-5px);
  }
  
  .quote-text {
    font-size: 18px;
    font-style: italic;
    margin-bottom: 10px;
    color: #333;
  }
  
  .quote-book {
    font-weight: bold;
    margin-bottom: 5px;
    color: #444;
    text-align: right;
  }
  
  .quote-author {
    color: #555;
    text-align: right;
  }
  </style>