import { Component, OnInit, Input } from '@angular/core';
import { HeaderComponent } from '../header/header.component';
import { JukeBikeService, JukeSearchResult, JukeTrack } from '../jukebike.service'

@Component({
  selector: 'app-song-search',
  templateUrl: './song-search.component.html',
  styleUrls: ['./song-search.component.css']
})
export class SongSearchComponent implements OnInit {

  searchInput: string = ''
  resultList: Array<JukeSearchResult> = []

  constructor(
    private jukeBikeService: JukeBikeService
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
            this.resultList = newResultList
          })
      }
    }
  }

  wishSong(idx: int) {
    console.log('In wishSong :: idx = ' + idx)
  }

}
