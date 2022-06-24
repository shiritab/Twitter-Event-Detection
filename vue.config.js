
const path = require('path');
const fs = require('fs')

module.exports = {
    devServer: {
    port:8080,
    host: 'localhost',
    // key: fs.readFileSync('C:/Program Files/Git/usr/bin/privateKey.key'),
    // cert: fs.readFileSync('C:/Program Files/Git/usr/bin/certificate.crt'),
    // hotOnly: false,
    },
    configureWebpack: {
        module: {
            rules: [
                {
                    test: /\.md$/i,
                    use: ["raw-loader"],
                },
            ],
        },
      },
    
}
// key: fs.readFileSync('C:/Program Files/Git/usr/bin/privateKey.key'),
// cert: fs.readFileSync('C:/Program Files/Git/usr/bin/certificate.crt'),