import { Component, OnInit, Input } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { JukeBikeService, JukeTrack } from '../jukebike.service'

@Component({
  selector: 'app-wish-song',
  templateUrl: './wish-song.component.html',
  styleUrls: ['./wish-song.component.css']
})
export class WishSongComponent implements OnInit {

  myName = ''

  constructor(
    private jukeBikeService: JukeBikeService,
    private router: Router
  ) { }

  ngOnInit(): void {
  }

  currentWish = this.jukeBikeService.currentWish

  submitTrackWish() {
    /*
    // TODO remove
    this.songWish = new JukeTrack()
    this.songWish.name = 'Jay-Z - 99 Problems, but the bitch aint one ;-)'
    this.songWish.uri = 'spotify:track:7IdFdRlCjUi6kkhbPoRfnw'
    */
    console.log('In submitTrackWish :: currentWish = ' + JSON.stringify(this.currentWish))
    console.log(':: myName = ' + this.myName)

    this.jukeBikeService
      .wishTrack(
        this.currentWish.uri,
        this.myName
      )
      .then(newWishConf => {
        console.log('In submitTrackWish :: then :: newWishConf = ' + JSON.stringify(newWishConf))
        this.jukeBikeService.currentConfirmation = newWishConf
        this.router.navigate(['/confirm'])
      })
  }

}
