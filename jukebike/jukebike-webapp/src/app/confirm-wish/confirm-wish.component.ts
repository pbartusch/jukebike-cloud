import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { JukeBikeService } from '../jukebike.service'

@Component({
  selector: 'app-confirm-wish',
  templateUrl: './confirm-wish.component.html',
  styleUrls: ['./confirm-wish.component.css']
})
export class ConfirmWishComponent implements OnInit {

  queuePosition = -1
  readableMinutes = -1
  readableSeconds = -1

  constructor(
    private jukeBikeService: JukeBikeService
  ) { }

  ngOnInit(): void {
    let currentConfirmation = this.jukeBikeService.currentConfirmation
    this.queuePosition = currentConfirmation.queuePosition
    this.readableMinutes = Math.floor(currentConfirmation.secondsToWait / 60)
    this.readableSeconds = currentConfirmation.secondsToWait % 60
  }

}
