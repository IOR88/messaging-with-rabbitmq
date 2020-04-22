'use strict';
import axios from 'axios';
import {getCookie} from "../utils";
import qs from 'qs'

const COLLAGE_BASE_URL = 'http://localhost:8000/';

export const instance = axios.create({
  baseURL: COLLAGE_BASE_URL,
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

export const chat = {
    all: () => requestHandler({url: `${API}/chat/`, method: 'GET'})
};
