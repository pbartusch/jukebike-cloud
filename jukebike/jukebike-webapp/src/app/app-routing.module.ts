import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SongSearchComponent } from './song-search/song-search.component';
import { WishSongComponent } from './wish-song/wish-song.component';
import { ConfirmWishComponent } from './confirm-wish/confirm-wish.component';

const routes: Routes = [
  { path: 'search', component: SongSearchComponent },
  { path: 'wish', component: WishSongComponent },
  { path: 'confirm', component: ConfirmWishComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
