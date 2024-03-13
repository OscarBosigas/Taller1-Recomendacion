import { Injectable } from '@angular/core'
import { HttpClient, HttpErrorResponse} from '@angular/common/http'
import { catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';
import { Observable } from 'rxjs'
import { Artista } from './artista';
import { Usuario } from '../home/usuario';

@Injectable({
    providedIn: 'root'
})

export class ArtistaService {

    constructor (private http: HttpClient) {}

    public getRecomendaciones(usuario:Usuario):Observable<Artista[]>
    {
        return this.http.post<Artista[]>('http://127.0.0.1:5000/predict', usuario)
    }
}