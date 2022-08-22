import VagasRepository from '../../repositories/VagasRepository'
import ACTION_VAGA from '../action/vagaAction' 

let initState = {
    data : [],
    isLoading : false,
    vaga : {}
}

export const vagaReducer = (state = initState, action) => {
    switch(action.type){
        case ACTION_VAGA.REQUESTING :
            return {...state, isLoading : action.payload.isLoading}
        case ACTION_VAGA.RESOLVED :
            return {...state, data : action.data}
        case ACTION_VAGA.RESOLVED_ID :
            return {...state, vaga : action.data}
        case ACTION_VAGA.REJECT :
            return state
        default : 
            return state;
    }
}

class VagaReducer{
    static fetch = () => async(dispatch) => {
        try {
            const data = await VagasRepository.get()
            dispatch({
                type : ACTION_VAGA.RESOLVED,
                data : data,
            })
            console.log('executando try')
        } catch (error) {
            console.log(error, 'ERRO')
        }
    }

    static fetchId = (id) => async(dispatch) => {
        dispatch(ACTION_VAGA.requesting())
        try {
            const data = await VagasRepository.getId(id)
            dispatch({
                type : ACTION_VAGA.RESOLVED_ID,
                data : data,
            })
            dispatch(ACTION_VAGA.resoved_id(data))        
        } catch (error) {
            console.log(error)
        }
    }
}



export default VagaReducer