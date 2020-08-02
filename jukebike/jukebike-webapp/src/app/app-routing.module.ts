import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SongSearchComponent } from './song-search/song-search.component';
import { WishSongComponent } from './wish-song/wish-song.component';
import { ConfirmWishComponent } from './confirm-wish/confirm-wish.component';
import { AdminComponent } from './admin/admin.component';

const routes: Routes = [
  { path: '', redirectTo: '/search', pathMatch: 'full' },
  { path: 'search', component: SongSearchComponent },
  { path: 'wish', component: WishSongComponent },
  { path: 'confirm', component: ConfirmWishComponent },
  { path: 'admin', component: AdminComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {useHash: true})],
  exports: [RouterModule]
})
export class AppRoutingModule { }
