import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000';

export default class LotteriesService{

    constructor(){}

    getLotteries() {
        const url = `${API_URL}/api/lotteries/`;
        return axios.get(url).then(response => response.data);
    }
    getLotteriesByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    /*getLotteries(pk) {
        const url = `${API_URL}/api/lotteries_detail/${pk}`;
        return axios.get(url).then(response => response.data);
    }*/
    deleteLotteries(lottery){
        const url = `${API_URL}/api/lotteries_detail/${lottery.id}`;
        return axios.delete(url);
    }
    createLotteries(lottery){
        const url = `${API_URL}/api/lotteries/`;
        return axios.post(url,lottery);
    }
    updateLotteries(lottery){
        const url = `${API_URL}/api/lotteries_detail/${lottery.id}`;
        return axios.put(url,lottery);
    }
}