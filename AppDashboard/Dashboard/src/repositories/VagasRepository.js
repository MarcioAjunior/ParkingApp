import axios from "axios";
import Vagas from '../models/Vagas'

const url = 'http://127.0.0.1:5001/'

class VagasRepository{

    static get = () => new Promise(async(resolve, reject) => {
        const {data} = await axios.get(url)
        console.log(data.msg, typeof(data.msg))
        console.log(JSON.parse(data.msg))
        let stringToArray = JSON.parse(data.msg)
        let res = stringToArray.map((item) => item)
        console.log(res, 'MEU RES')
        console.log('alksjdlaskjdlaksjdlaskjdlakjsdlkasjdlkjasldkjasl')
        return resolve(res)          
    })

    static getId = (id) => new Promise(async(resolve, reject) => {
        const {data} = await axios.get(`${url}/${id}`)
        if (data.msg !== undefined){
            console.log(data.msg)
            return resolve(data.msg)
        }
      return reject(data)
    })

}
export default VagasRepository