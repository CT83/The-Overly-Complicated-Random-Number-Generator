import React from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      value: '',
      result: '-',
    }
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(e) {
    this.setState({ value: e.target.value });
  }

  buttonClick = (event) => {
    event.preventDefault()
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ seed: this.state.value })
    };
    var that = this;
    fetch('/api/tasks', requestOptions)
      .then(response => response.json())
      .then(data => {
        this.setState({ job_id: data.job_id });
        setTimeout(function () {
          fetch('/api/tasks?job_key=' + that.state.job_id)
            .then(response => response.json()).then(result => {
              that.setState({ result: result.result });
            })
        }, 5000);
      });

  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <input type="number" value={this.state.value} onChange={this.handleChange} placeholder="Enter Random Seed" />
          <a className="App-link" href="" onClick={this.buttonClick}>
            Generate a Random Number!
          </a>
          <h3>Result: {this.state.result}</h3>
        </header>
      </div>
    );

  }
}

export default App;
