import css from '../css/base.css';
import 'regenerator-runtime/runtime';
import React, {Component, Fragment} from 'react';
import ReactDOM from 'react-dom';
import lodash from 'lodash';
import {users, rooms} from './core/api';
import {createSocket} from "./core/sockets";


class App extends Component {

    constructor(props) {
        super(props);
        this.state = {
            users: [],
            rooms: [],
            connection: null
        };
    }

    componentWillMount() {
        //get users
        users
            .all()
            .then((response)=>{
                this.setState({users: response.data});
            });

        //get rooms
        rooms
            .all()
            .then((response)=>{
                this.setState({rooms: response.data});
            });

        //create websocket connection
        const connection = createSocket();
        this.setState({connection});
    }

    render(){

        return <div id={"main"}>
            <header>Messaging with RabbitMQ</header>
            <p>Available users: {JSON.stringify(this.state.users)}</p>
            <p>Available rooms: {JSON.stringify(this.state.rooms)}</p>

        </div>
    }

}


ReactDOM.render(<App/>, document.getElementById('application'));