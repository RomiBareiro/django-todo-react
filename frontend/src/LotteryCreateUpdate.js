import React, { Component } from 'react';
import LotteriesService from './LotteriesService';

const lotteriesService = new LotteriesService();

class LotteryCreateUpdate extends Component {
    constructor(props) {
        super(props);

        this.handleSubmit = this.handleSubmit.bind(this);
      }

      componentDidMount(){
        const { match: { params } } = this.props;
        if(params && params.id)
        {
          lotteriesService.getLottery(params.id).then((c)=>{
            this.tipo_quiniela.value = c.tipo_quiniela;
            this.nombre_sorteo.value = c.nombre_sorteo;
            this.fecha.value = c.fecha;
            this.letras.value = c.letras;
          })
        }
      }

      handleCreate(){
        lotteriesService.createLottery(
          {
            "tipo_quiniela": this.tipo_quiniela.value,
            "nombre_sorteo": this.nombre_sorteo.value,
            "fecha": this.fecha.value,
            "timezone_type": this.timezone_type.value,
            "timezone": this.timezone.value,
            "letras": this.letras.value
        }
        ).then((result)=>{
          alert("Lottery created!");
        }).catch(()=>{
          alert('There was an error! Please re-check your form.');
        });
      }
      handleUpdate(pk){
        lotteriesService.updateLottery(
          {
            "id": pk,
            "tipo_quiniela": this.tipo_quiniela.value,
            "nombre_sorteo": this.nombre_sorteo.value,
            "fecha": this.fecha.value,
            "timezone_type": this.timezone_type.value,
            "timezone": this.timezone.value,
            "letras": this.letras.value
        }
        ).then((result)=>{
          console.log(result);
          alert("Lottery updated!");
        }).catch(()=>{
          alert('There was an error! Please re-check your form.');
        });
      }
      handleSubmit(event) {
        const { match: { params } } = this.props;

        if(params && params.pk){
          this.handleUpdate(params.pk);
        }
        else
        {
          this.handleCreate();
        }

        event.preventDefault();
      }

      render() {
        return (
          <form onSubmit={this.handleSubmit}>
          <div className="form-group">
            <label>
              Tipo de Quiniela:</label>
              <input className="form-control" type="text" ref='tipo_quiniela' />

            <label>
              Nombre Sorteo:</label>
              <input className="form-control" type="text" ref='nombre_sorteo'/>

            <label>
              Fecha:</label>
              <input className="form-control" type="text" ref='fecha' />

            <label>
              timezone_type:</label>
              <input className="form-control" type="text" ref='timezone_type' />

            <label>
                timezone:</label>
              <input className="form-control" type="text" ref='timezone' />

            <label>
              Letras:</label>
              <textarea className="form-control" ref='letras' ></textarea>


            <input className="btn btn-primary" type="submit" value="Submit" />
            </div>
          </form>
        );
      }
}

export default LotteryCreateUpdate;