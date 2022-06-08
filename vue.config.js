
//   module.exports = {
//     devServer: {
//       host: '10.0.0.128',
//       port: 443, 
//     },
//   }


//   const fs = require('fs')

// module.exports = {
//     devServer: {
//         open: process.platform === 'darwin',
//         hotOnly: false,
//         host: '0.0.0.0',
//         https:{

//         },
//         port: 80, 
//         }
// }

const fs = require('fs')

module.exports = {
    devServer: {
    port:8080,
    host: 'localhost',
    // key: fs.readFileSync('C:/Program Files/Git/usr/bin/privateKey.key'),
    // cert: fs.readFileSync('C:/Program Files/Git/usr/bin/certificate.crt'),
    // hotOnly: false,
    },
    // configureWebpack: {
    //     module: {
    //         rules: [
    //             {
    //               test: /\.md$/i,
    //               use: 'raw-loader',
    //             },
    //         ],
    //     },
    //   },
    
}
// key: fs.readFileSync('C:/Program Files/Git/usr/bin/privateKey.key'),
// cert: fs.readFileSync('C:/Program Files/Git/usr/bin/certificate.crt'),