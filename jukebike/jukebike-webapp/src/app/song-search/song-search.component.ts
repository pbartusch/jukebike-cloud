import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';
import { HeaderComponent } from '../header/header.component';
import { JukeBikeService, JukeTrack } from '../jukebike.service'

@Component({
  selector: 'app-song-search',
  templateUrl: './song-search.component.html',
  styleUrls: ['./song-search.component.css']
})
export class SongSearchComponent implements OnInit {

  searchInput: string = ''
  resultList: Array<JukeTrack> = []
  showHint = true

  constructor(
    private jukeBikeService: JukeBikeService,
    private router: Router
  ) { }

  ngOnInit(): void {
  }

  instantSearch(event) {
    if(this.searchInput != event.target.value) {
      this.searchInput = event.target.value
      this.resultList = []
      console.log('In instantSearch (value changed!) :: searchInput = ' + this.searchInput)
      if(this.searchInput.trim().length > 2) {
        this.jukeBikeService
          .searchSong(this.searchInput)
          .then(newResultList => {
            console.log(':: newResultList = ' + newResultList)
            this.showHint = false
            this.resultList = newResultList
          })
      } else {
        this.showHint = true
      }
    }
  }

  wishSong(idx) {
    console.log('In wishSong :: idx = ' + idx)
    this.jukeBikeService.currentWish = this.resultList[idx]
    this.router.navigate(['/wish'])
  }

}
