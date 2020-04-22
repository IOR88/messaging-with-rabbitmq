import css from '../css/base.css';
import 'regenerator-runtime/runtime';
import React, {Component, Fragment} from 'react';
import ReactDOM from 'react-dom';
import lodash from 'lodash';


class App extends Component {

    constructor(props) {
        super(props);
        this.state = {};
    }

    componentWillMount() {
        const {dispatch} = this.props;
        dispatch(actions.containers.read());
    }

    render(){

        return <div id={"main"}>
            CHAT
        </div>
    }

}


ReactDOM.render(<App/>, document.getElementById('application'));