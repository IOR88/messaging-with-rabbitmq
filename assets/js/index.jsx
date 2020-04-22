import css from '../css/base.css';
import 'regenerator-runtime/runtime';
import React, {Component, Fragment} from 'react';
import ReactDOM from 'react-dom';
import lodash from 'lodash';
import {users} from './core/api';


class App extends Component {

    constructor(props) {
        super(props);
        this.state = {
            users: []
        };
    }

    componentWillMount() {
        //get users
        users
            .all()
            .then((response)=>{
                this.setState({users: response.data});
            });

    }

    render(){

        return <div id={"main"}>
            <header>Messaging with RabbitMQ</header>
            <p>Available users: {JSON.stringify(this.state.users)}</p>

        </div>
    }

}


ReactDOM.render(<App/>, document.getElementById('application'));