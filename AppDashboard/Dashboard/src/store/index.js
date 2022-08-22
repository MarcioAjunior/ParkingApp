import { combineReducers } from 'redux'

import {vagaReducer} from './reducer/vagaReducer'

const mainReducer = combineReducers({
    vagas : vagaReducer
})

export default mainReducer