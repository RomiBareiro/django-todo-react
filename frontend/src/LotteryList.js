import  React, { Component } from  'react';
import  LotteriesService  from  './LotteriesService';

const  lotteriesService  =  new  LotteriesService();

class  LotteryList  extends  Component {

constructor(props) {
    super(props);
    this.state  = {
        lotteries: [],
        nextPageURL:  ''
    };
    this.nextPage  =  this.nextPage.bind(this);
    this.handleDelete  =  this.handleDelete.bind(this);
}

componentDidMount() {
    var  self  =  this;
    lotteriesService.getLotteries().then(function (result) {
        console.log(result);
        self.setState({ lotteries:  result.data, nextPageURL:  result.nextlink})
    });
}
handleDelete(e,pk){
    var  self  =  this;
    lotteriesService.deleteLotteries({id :  pk}).then(()=>{
        var  newArr  =  self.state.lotteries.filter(function(obj) {
            return  obj.pk  !==  pk;
        });

        self.setState({lotteries:  newArr})
    });
}

nextPage(){
    var  self  =  this;
    console.log(this.state.nextPageURL);
    lotteriesService.getLotteriesByURL(this.state.nextPageURL).then((result) => {
        self.setState({ lotteries:  result.data, nextPageURL:  result.nextlink})
    });
}
render() {

    return (
        <div  className="lottery--list">
            <table  className="table">
            <thead  key="thead">
            <tr>
                <th>ID</th>
                <th>Nombre Sorteo</th>
                <th>Tipo Quiniela</th>
                <th>Fecha</th>
                <th>Letras</th>
                <th>Premios</th>
                <th>Pozo Proximo</th>
                <th>#1</th>
                <th>#2</th>
                <th>#3</th>
                <th>#4</th>
                <th>#5</th>
            </tr>
            </thead>
            <tbody>
            {this.state.lotteries.map( c  =>
                <tr  key={c.id}>
                <td>{c.id}  </td>
                <td>{c.nombre_sorteo}</td>
                <td>{c.tipo_quiniela}</td>
                <td>{c.fecha}</td>
                <td>{c.letras}</td>
                <td>{c.premios}</td>
                <td>{c.pozo_proximo}</td>
                <td>{c.numero1}</td>
                <td>{c.numero2}</td>
                <td>{c.numero3}</td>
                <td>{c.numero4}</td>
                <td>{c.numero5}</td>
                <td>
                <button  onClick={(e)=>  this.handleDelete(e,c.pk) }> Delete</button>
                <a  href={"/api/lotteries/" + c.pk}> Update</a>
                </td>
            </tr>)}
            </tbody>
            </table>
            <button  className="btn btn-primary"  onClick=  {  this.nextPage  }>Next</button>
        </div>
        );
  }
}
export  default  LotteryList;