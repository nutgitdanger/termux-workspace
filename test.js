const bcrypt = require('bcryptjs');

const hash = bcrypt.hashSync("123456", 10);
console.log(hash);

console.log(bcrypt.compareSync("123456", hash));
