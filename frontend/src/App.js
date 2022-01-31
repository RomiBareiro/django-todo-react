import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom'
import { Route } from 'react-router-dom'

import  LotteriesList from './LotteryList'
import  LotteryCreateUpdate  from './LotteryCreateUpdate'
import './App.css';

const BaseLayout = () => (
  <div className="container-fluid">
<nav className="navbar navbar-expand-lg navbar-light bg-light">
  <a className="navbar-brand" href="127.0.0.1:3000">Django React Demo</a>
  <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
    <span className="navbar-toggler-icon"></span>
  </button>
  <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
    <div className="navbar-nav">
      <a className="nav-item nav-link" href="/api/lotteries/">Lotteries</a>
      <a className="nav-item nav-link" href="/api/lotteries/">CREATE Lottery</a>

    </div>
  </div>
</nav>

    <div className="content">
      <Route path="/api/lotteries/" exact component={LotteriesList} />
      <Route path="/api/lotteries/"  component={LotteryCreateUpdate} />
      <Route path="/api/lotteries/:pk" exact component={LotteryCreateUpdate} />

    </div>

  </div>
)

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <BaseLayout/>
      </BrowserRouter>
    );
  }
}

export default App;