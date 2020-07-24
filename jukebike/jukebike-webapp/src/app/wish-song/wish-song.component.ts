import { Component, OnInit, Input } from '@angular/core';
import { JukeBikeService, JukeSearchResult, JukeTrack } from '../jukebike.service'

@Component({
  selector: 'app-wish-song',
  templateUrl: './wish-song.component.html',
  styleUrls: ['./wish-song.component.css']
})
export class WishSongComponent implements OnInit {

  @Input songWish: JukeTrack = null;

  constructor(
    private jukeBikeService: JukeBikeService
  ) { }

  ngOnInit(): void {
  }

  submitTrackWish() {
    // TODO remove
    this.songWish = new JukeTrack()
    this.songWish.name = 'Jay-Z - 99 Problems, but the bitch aint one ;-)'
    this.songWish.uri = 'spotify:track:7IdFdRlCjUi6kkhbPoRfnw'
    let username = "Paule Meister"

    console.log('In submitTrackWish :: songWish.uri = ' + this.songWish.uri)
    console.log(':: username = ' + username)

    this.jukeBikeService.wishTrack(
      this.songWish.uri,
      username
    )
  }

}
