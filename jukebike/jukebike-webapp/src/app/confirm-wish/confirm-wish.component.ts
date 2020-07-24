import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { JukeBikeService } from '../jukebike.service'

@Component({
  selector: 'app-confirm-wish',
  templateUrl: './confirm-wish.component.html',
  styleUrls: ['./confirm-wish.component.css']
})
export class ConfirmWishComponent implements OnInit {

  constructor(
    private jukeBikeService: JukeBikeService
  ) { }

  ngOnInit(): void {
  }

  currentConfirmation = this.jukeBikeService.currentConfirmation

}
