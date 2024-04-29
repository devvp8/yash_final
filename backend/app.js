const express = require('express');
const app = express();
const cors = require('cors');
const { c, cpp, node, python, java } = require('compile-run');
const fs = require('fs');
const util = require('util');
const readFileAsync = util.promisify(fs.readFile);
// code to run

app.use(cors());
app.use(express.json());

app.post('/compile', async (req, res) => {
    try {
        const { code, lang } = req.body;
        fs.writeFileSync('temp.txt', code);
        const data = await readFileAsync('temp.txt', 'utf8');
        let result
        if (lang==='Python')
        result = await python.runSource(data)
        else if (lang==='Java')
        result=await java.runSource(data)
        else if (lang==='Cpp')
        {
        result = await cpp.runSource(data, {
            compilationPath: "C:\\Users\\Dev Atul Patel\\Downloads\\msys2-x86_64-20240113.exe"
        });
        console.log(result);}
        else if (lang==='c')
        result=await c.runSource(data)
        else if(lang==='JavaScript')
        result=await node.runSource(data)
        console.log(result)
        res.status(200).json({ output: result.stdout, error: result.stderr });
    } catch (error) {
        console.log(error.message);
        res.status(400).json({ message: error.message });
    }
});

app.listen(5000, () => {
    console.log('node on 5000...');
});
