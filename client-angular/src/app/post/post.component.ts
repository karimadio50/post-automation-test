import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';
import { FormControl, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldControl, MatFormFieldModule } from '@angular/material/form-field';

import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';

import { RouterOutlet } from '@angular/router';
import { PostService } from '../services/post.service';


@Component({
  selector: 'app-post',
  standalone: true,
  imports:[RouterOutlet,
    FormsModule, MatFormFieldModule, MatInputModule, 
    ReactiveFormsModule
  ],

  providers:[PostService],

  changeDetection : ChangeDetectionStrategy.OnPush,
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.scss']
})
export class PostComponent implements OnInit {
  
  imageInput = new FormControl('', [Validators.required, ]);
  promptInput = new FormControl('', [Validators.required, ]);
  promptGenerated = new FormControl('', [Validators.required, ]);


  imageUrl!: string;
  constructor(private service: PostService) { }

  ngOnInit():void {
    this.imageUrl = 'http://127.0.0.1:8000/get_files/astronaut';

  }
  generateImagePost(){
    if (this.imageInput.invalid){
      return
    }
    console.log('oui')
  }

  generateTextPost(){
    if (this.promptInput.invalid){
      return
    }
    console.log(this.promptInput.value)
  }

  TextGenerated(){
    if (this.promptGenerated.invalid){
      return
    }
    console.log('oui')
  }

}
