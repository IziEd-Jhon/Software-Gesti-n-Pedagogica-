const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave:false
})
module.exports = {
  devServer: {
      proxy: 'https://localhost:8000'
  } }
