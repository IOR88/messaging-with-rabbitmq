'use strict';
import axios from 'axios';
import {getCookie} from "../utils";
import qs from 'qs';

const MWR_BASE_URL = 'http://localhost:8000/';

export const instance = axios.create({
  baseURL: MWR_BASE_URL,
  headers: {
      'X-CSRFToken': getCookie('csrftoken')
  },
 paramsSerializer: (params)=> {
    return qs.stringify(params, { arrayFormat: 'comma', encode: false  });
  }
});



async function requestHandler({url, method, data, params}){
    try {
        const response = await instance.request({url, method, data, params});
        return {error:false, data: response.data};
    } catch(err){
        return {error:true, data: err.message};
    }
}

const API = 'api';

export const users = {
    all: () => requestHandler({url: `${API}/chat/users/active`, method: 'GET'})
};

export const messages = {
    all: (params) => requestHandler({url: `${API}/chat/messages/`, method: 'GET', params}),
    post: (data) => requestHandler({url: `${API}/chat/messages/`, method: 'POST', data})
};

export const rooms = {
    all: (params) => requestHandler({url: `${API}/chat/rooms/`, method: 'GET', params})
};