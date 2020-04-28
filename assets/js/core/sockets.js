import io from 'socket.io-client';

const MWR_BASE_URL = 'http://localhost:8888/';

function createSocket(){
    return io.connect(`${MWR_BASE_URL}`);
}

export {createSocket}