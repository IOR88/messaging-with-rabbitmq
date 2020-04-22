const webpack = require('webpack'),
    path = require('path');


const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const config = {
    mode: 'development',
    devtool: 'eval-source-map',
    //The base directory, an absolute path, for resolving entry points and loaders from configuration.
    context: path.resolve(__dirname, 'assets'),
    entry: './js/index.jsx',
    output: {
        //The output directory as an absolute path.
        path: path.resolve(__dirname, 'src/mwr/static'),
        filename: 'bundle.js',
        //This option specifies the public URL of the output directory when referenced in a browser.
        //publicPath attribute is used by HtmlWebpackPlugin when injecting scripts and stylesheets into the html file
        //in development env we use webpack-dev-server
        publicPath: 'http://localhost:9000/dist/'
    },
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ["@babel/preset-env", "@babel/preset-react"]
                    }
                },

                include: [path.resolve(__dirname, 'assets/js')]

            },
            {
                test: /\.css$/,
                use: [MiniCssExtractPlugin.loader, 'css-loader', {
                    loader: 'postcss-loader',
                    options: {
                        plugins: () => [
                            require('autoprefixer')
                        ],
                        sourceMap: true
                    }
                }]
            },

            {
                test: /\.less/,
                use: [MiniCssExtractPlugin.loader, 'css-loader', {
                    loader: 'postcss-loader',
                    options: {
                        plugins: () => [
                            require('autoprefixer')
                        ],
                        sourceMap: true
                    }
                }, 'less-loader']
            },
            {
                test: /\.scss/,
                use: [MiniCssExtractPlugin.loader, 'css-loader', {
                    loader: 'postcss-loader',
                    options: {
                        plugins: () => [
                            require('autoprefixer')
                        ],
                        sourceMap: true
                    }
                }, 'sass-loader']
            },

            {
                test: /\.(jpe?g|png|gif|svg)$/i,
                loader: 'file-loader'
            },
            {
                test: /\.(woff|woff2|eot|ttf|otf)$/,
                loader: 'file-loader'
            }
        ]
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css', '.less', '.scss'],
        modules: [
            path.resolve(__dirname, 'assets'),
            path.resolve(__dirname, 'node_modules')
        ]
    },
    plugins: [
        new MiniCssExtractPlugin({
          filename: '[name].css',
          chunkFilename: '[id].css',
        })
    ],

    externals: {

    },

    watchOptions: {
        //For some systems, watching many file systems can result in a lot of CPU or memory usage.
        // It is also possible to use anymatch patterns:
        //ignored: "files/**/*.js"
        ignored: /node_modules/
    },

    //no output bundles, webpack-dev-server keeps transcompiled files in memory
    devServer: {
        publicPath: '/dist/',
        contentBase: path.resolve('.'),
        port: 9000,
        //quiet: true, //no logs to console
        // --hot --inline (has to be added to cli)
        hot: true,
        watchOptions: {
            ignored: /node_modules/
        },
        headers: {
            'Access-Control-Allow-Origin': '*'
        }
    }
};


config.plugins.push(new webpack.NamedModulesPlugin());
config.plugins.push(new webpack.HotModuleReplacementPlugin());


module.exports = config;