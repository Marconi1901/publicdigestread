const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  chainWebpack: (config) => {
    config.plugin('html').tap((args) => {
      args[0].title = `书摘集锦`
      return args
    })
  },
  devServer: {
    port: 3000,  // 将端口设置为 3000
    host: '0.0.0.0',  // 允许局域网访问，如果不需要可以忽略此项
    proxy: {
      '/api': {
        target: 'http://localhost:8080', // 后端 API 地址
        changeOrigin: true,
        pathRewrite: {
          '^/api': '' // 移除 /api 前缀
        }
      }
    }
  }
})
