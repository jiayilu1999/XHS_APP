module.exports = {
  publicPath: '/',
  outputDir: 'dist',
  assetsDir: 'static',
  devServer: {
    port: 63342,
    host: 'localhost',
    open: true,
    historyApiFallback: true,
    static: {
      directory: __dirname,
      publicPath: '/'
    }
  },
  configureWebpack: {
    output: {
      publicPath: '/',
      filename: '[name].js',
      chunkFilename: '[name].js'
    },
    resolve: {
      alias: {
        '@': __dirname
      }
    }
  },
  "h5": {
    "router": {
      "mode": "history",
      "base": "/"
    },
    "devServer": {
      "port": 63342,
      "disableHostCheck": true
    }
  }
} 