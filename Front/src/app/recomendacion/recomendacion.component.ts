import { Component, OnInit } from '@angular/core';
import { RegistroService } from '../registro/registro.service';
import { Usuario } from '../home/usuario';
import { LogInService } from '../home/login.service';
import { Artista } from './artista';
import { ArtistaService } from './artista.service';

@Component({
  selector: 'app-recomendacion',
  templateUrl: './recomendacion.component.html',
  styleUrls: ['./recomendacion.component.css']
})
export class RecomendacionComponent implements OnInit {

  constructor(private artistaService: ArtistaService, private login: LogInService) { }

  id: string = '';
  artistas: Array<Artista> =[new Artista('','')]

  ngOnInit(): void {
    this.id = this.login.getId2();
    this.artistaService.getEventos(new Usuario(this.id,'','','','','')).subscribe(res =>{
      this.artistas = res;
    })
  }

}
