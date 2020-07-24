import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule }    from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SongSearchComponent } from './song-search/song-search.component';
import { WishSongComponent } from './wish-song/wish-song.component';
import { ConfirmWishComponent } from './confirm-wish/confirm-wish.component';
import { HeaderComponent } from './header/header.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { JukeBikeService } from './jukebike.service';

@NgModule({
  declarations: [
    AppComponent,
    SongSearchComponent,
    WishSongComponent,
    ConfirmWishComponent,
    HeaderComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    HttpClientModule
  ],
  providers: [
    JukeBikeService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
