class ACTION_VAGA{
    static REQUESTING = 'REQUESTING'
    static RESOLVED = 'RESOLVED'
    static RESOLVED_ID = 'RESOLVED_ID'
    static REJECT = 'REJECT'

    static requesting = function(){
        return{
            type : ACTION_VAGA.REQUESTING,
            payload : {
                isLoading : true,
                error : null,
                data : {}
            }
        }
    }

    static resoved = function(data){
        return {
            type : ACTION_VAGA.RESOLVED,
            data : [...data]
        }
    }

    static resoved_id = function(data){
        return {
            type : ACTION_VAGA.RESOLVED_ID,
            data : data
        }
    }

    static reject = function(data){
        return {
            type : ACTION_VAGA.REJECT,
            data
        }
    }

}

export default ACTION_VAGA