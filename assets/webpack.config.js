var path = require("path");
var webpack = require('webpack')

module.exports = {

    context: __dirname,
    entry:  {
        calendar: './calendar',
    },
    output: {
        path: path.resolve('./bundles/'),
        filename: '[name].js',
    },
    plugins: [],
    mode: 'production',
    module: {
        rules: [
            {
                test: /\.css$/,
                'loader': 'style-loader'
            },
            {
                test: /\.css$/,
                loader: 'css-loader',
                query: {
                    modules: true,
                    localIdentName: '[name]__[local]__[hash:64:5]'
                }
            },
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
                query: {
                    presets: ['stage-2','react']//stage 2 for class level attrs and autobind
                }
            }
        ]
    },

    resolve: {
        extensions: [ '.js', '.jsx']
    },
}