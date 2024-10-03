<template>
    <div>
      <h2>Book Quotes List</h2>
      
      <ul>
        <li v-for="(quote, index) in quotes" :key="index">
          <blockquote>
            "{{ quote.text }}"
          </blockquote>
          <p>- <em>{{ quote.author }}</em> from <strong>{{ quote.book }}</strong></p>
        </li>
      </ul>
  
      <h3>Add a new Quote</h3>
      <form @submit.prevent="addQuote">
        <label for="text">Quote:</label>
        <input v-model="newQuote.text" id="text" required />
  
        <label for="author">Author:</label>
        <input v-model="newQuote.author" id="author" required />
  
        <label for="book">Book:</label>
        <input v-model="newQuote.book" id="book" required />
  
        <button type="submit">Add Quote</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        // 书摘数据
        quotes: [
          { text: 'The only limit to our realization of tomorrow is our doubts of today.', author: 'Franklin D. Roosevelt', book: 'Speeches' },
          { text: 'In the middle of difficulty lies opportunity.', author: 'Albert Einstein', book: 'Letters' }
        ],
        // 表单输入数据
        newQuote: {
          text: '',
          author: '',
          book: ''
        }
      };
    },
    methods: {
      // 添加书摘方法
      addQuote() {
        // 将新书摘添加到书摘列表
        this.quotes.push({ ...this.newQuote });
  
        // 重置表单
        this.newQuote.text = '';
        this.newQuote.author = '';
        this.newQuote.book = '';
      }
    }
  };
  </script>
  
  <style scoped>
  form {
    margin-top: 20px;
  }
  
  input {
    margin-bottom: 10px;
    padding: 5px;
    display: block;
  }
  
  button {
    padding: 10px;
    background-color: #42b983;
    color: white;
    border: none;
    cursor: pointer;
  }
  
  blockquote {
    font-style: italic;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    margin-bottom: 20px;
    background-color: #f0f0f0;
    padding: 15px;
    border-radius: 5px;
  }
  
  li blockquote {
    margin: 0;
    font-size: 1.2em;
  }
  </style>  