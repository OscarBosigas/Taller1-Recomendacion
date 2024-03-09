import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { RegistroComponent } from './registro/registro.component';
import { RecomendacionComponent } from './recomendacion/recomendacion.component';

const routes: Routes = [
  { path: '', component: HomeComponent},
  { path: 'registro', component: RegistroComponent},
  { path: 'recomendacion', component: RecomendacionComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
